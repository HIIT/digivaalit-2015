create_dtm <- function( path ) {

  library(tm)
  library(slam)

  a <- Corpus( DirSource( path, encoding = "UTF-8", recursive = T ) )

  stop1 <- scan('stop_generic.txt', what = list(""), sep = '\n' )
  stop2 <- c()
##  stop2 <- scan('stop_digivaalit.txt', what = list(""), sep = '\n' )
  stop <- c( stopwords("finnish") , stop1, stop2 , recursive=T )

  ## bunch of cleanup and transformations
  a <- tm_map(a, removeNumbers, mc.cores=1 )
  a <- tm_map(a, stripWhitespace, mc.cores=1 )
  a <- tm_map(a, removePunctuation, mc.cores=1 )
  a <- tm_map(a, content_transformer(tolower), mc.cores=1 )
  a <- tm_map(a, removeWords, stop )

  ## compute word frequencies
  dtm1 <-DocumentTermMatrix(a)

  frequency <- col_sums( dtm1 , na.rm = T )
  frequency <- sort(frequency, decreasing=TRUE)

  ## choose removal boundaries for further data analysis

  upper = floor( length( frequency ) * .001 )
  ##upper = Inf
  lower = floor( length( frequency) * .9 )
  
  upper = frequency[ upper ]
  lower = frequency[ lower ]
  
  upper = as.integer( upper )
  lower = as.integer( lower ) + 1

  dtm2 = DocumentTermMatrix( a , control = list( bounds = list( global = c( lower, upper ) ) ) )

  ## throw away columns with 0 indicators
  dtm3 <- dtm2[ row_sums( dtm2 ) > 0, ]

  dtm <- dtm3

  return( dtm )

}

create_model <- function( dtm, k ) {

   library(topicmodels)

   ## fix randomness
   set.seed( 1 )

   burnin = 1000
   iter = 1000
   keep = 50

   model <- LDA( dtm , k = k, method = "Gibbs", control =  list(burnin = burnin, iter = iter, keep = keep) )

   return( model )

}

check_fitness_ll <- function( model ) {

  ## TODO: could we just use logLik-methods?

  library(topicmodels)
  library(Rmpfr)

  burnin = 1000
  iter = 1000
  keep = 50

  ll <- model@logLiks[ -c(1:(burnin/keep)) ]

  precision = 2000L
  llMed <- median( ll )
  ll = as.double( llMed - log( mean( exp( -mpfr(ll , prec = precision) + llMed ) ) ) )

  return( ll )

}


check_fitness_model <- function( model ) {

  library(topicmodels)
  library(Rmpfr)

  burnin = 1000
  iter = 1000
  keep = 50

  k <- model@k

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
