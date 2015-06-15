create_dtm <- function( path ) {

  library(tm)

  a <- Corpus( DirSource( path ) )

  a <- tm_map(a, removeNumbers)
  a <- tm_map(a , stripWhitespace)
  a <- tm_map(a, removePunctuation)
  a <- tm_map(a, content_transformer(tolower) )
  a <- tm_map(a, removeWords, stopwords("finnish") )
  dtm <-DocumentTermMatrix(a)

  rowTotals <- apply(dtm , 1, sum)
  dtm.new   <- dtm[rowTotals> 0, ]

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

  model <- create_model( dtm , k )
  ll <- model@logLiks[ -c(1:(burnin/keep)) ]

  precision = 2000L
  llMed <- median( ll )
  ll = as.double( llMed - log( mean( exp( -mpfr(ll , prec = precision) + llMed ) ) ) )

  return( ll )

}
