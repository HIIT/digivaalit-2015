create_dtm <- function( path ) {

  library(topicmodels)
  library(tm)

  a <- Corpus( DirSource( path ) )

  a <- tm_map(a, removeNumbers)
  a <- tm_map(a , stripWhitespace)
  a <- tm_map(a, removePunctuation)
  a <- tm_map(a, content_transformer(tolower) )
  stopwords("finnish")
  a <- tm_map(a, removeWords, stopwords("finnish") )
  dtm <-DocumentTermMatrix(a)

  rowTotals <- apply(dtm , 1, sum)
  dtm.new   <- dtm[rowTotals> 0, ]

  ## save data for further use
  save( dtm.new , dtm , file = paste( path , '.rdata', sep = '' ) )
  return dtm.new

}

check_number_of_topics <- function( dtm , maxk = 250 ) {

  library(topicmodels)
  library(Rmpfr)

  burnin = 1000
  iter = 1000
  keep = 50

  result <- data.frame( 'k' = integer(0), 'll' = integer(0) )

  ## for memory restrictions, lets run this in separate sets
  for( i in 0: round( maxk / 10 ) ) {

    sequ <- seq( i * 10 + 1 , ( i + 1) * 10  )
    fitted_many <- lapply( sequ, function(k) {
  	   print(k);
  	    LDA( dtm.new , k = k, method = "Gibbs", control = list(burnin = burnin, iter = iter, keep = keep) )
    } )
    logLiks_many <- lapply(fitted_many, function(L)  L@logLiks[-c(1:(burnin/keep))] )

    harmonicMean <- function(logLikelihoods, precision=2000L) {
      llMed <- median(logLikelihoods)
      as.double(llMed - log(mean(exp(-mpfr(logLikelihoods, prec = precision) + llMed))))
    }

    hm_many <- sapply(logLiks_many, function(h) harmonicMean(h))


    k = sequ[which.max(hm_many)]
    ll = max( hm_many )

    result <- rbind( result, c( k , ll) ) )

  }

  return result;

}
