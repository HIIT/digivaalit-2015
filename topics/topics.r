create_dtm <- function( path ) {

  library(tm)
  library(Matrix)

  a <- Corpus( DirSource( path, encoding = "UTF-8" ) )

  ## bunch of cleanup and transformations
  a <- tm_map(a, removeNumbers, mc.cores=1 )
  a <- tm_map(a, stripWhitespace, mc.cores=1 )
  a <- tm_map(a, removePunctuation, mc.cores=1 )
  a <- tm_map(a, tolower, mc.cores=1 )
  a <- tm_map(a, function(x) iconv(x, to='UTF-8', sub='byte'), mc.cores=1 )
  a <- tm_map(a, removeWords, stopwords("finnish"), mc.cores=1 )

  ## transform back to plaintext documents
  a <- tm_map(a, PlainTextDocument)

  ## compute document-term
  dtm <-DocumentTermMatrix(a) ## , control = list( bounds = list( global = c( minDocFreq, maxDocFreq ) ) ) )

  ## totals <- apply(dtm , 1, sum) ## wont work on large sparse matrix
  totals <- sparseMatrix( dtm$i, dtm$j, x=dtm$v )
  dtm.new <- dtm[ rowSums( totals ) > 0, ]

  ## save data for further use
  ## save( dtm.new , dtm , file = paste( path , '.rdata', sep = '' ) )
  return( dtm.new )

}

create_model <- function( dtm, k ) {

   library(topicmodels)

   burnin = 1000
   iter = 1000
   keep = 50

   model <- LDA( dtm , k = k, method = "Gibbs", control =  list(burnin = burnin, iter = iter, keep = keep) )

   return( model )

}

check_fitness <- function( dtm , k ) {

  library(topicmodels)
  library(Rmpfr)

  burnin = 1000
  iter = 1000
  keep = 50

  model <- create_model( dtm , k )
  ll <- model@logLiks[ -c(1:(burnin/keep)) ]

  precision = 2000L
  llMed <- median( ll )
  ll = as.double( llMed - log( mean( exp( -mpfr(ll , prec = precision) + llMed ) ) ) )

  return( ll )

}


## from http://www.r-bloggers.com/a-link-between-topicmodels-lda-and-ldavis/

visualize_topicmodel <- function(fitted, corpus, doc_term){
    # Required packages
    library(topicmodels)
    library(dplyr)
    library(stringi)
    library(tm)
    library(LDAvis)

    # Find required quantities
    phi <- posterior(fitted)$terms %>% as.matrix
    theta <- posterior(fitted)$topics %>% as.matrix
    vocab <- colnames(phi)
    doc_length <- vector()
    for (i in 1:length(corpus)) {
        temp <- paste(corpus[[i]]$content, collapse = ' ')
        doc_length <- c(doc_length, stri_count(temp, regex = '\\S+'))
    }
    temp_frequency <- inspect(doc_term)
    freq_matrix <- data.frame(ST = colnames(temp_frequency),
                              Freq = colSums(temp_frequency))
    rm(temp_frequency)

    # Convert to json
    json_lda <- LDAvis::createJSON(phi = phi, theta = theta,
                            vocab = vocab,
                            doc.length = doc_length,
                            term.frequency = freq_matrix$Freq)

    return(json_lda)
}
