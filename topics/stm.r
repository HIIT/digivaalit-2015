create_model <- function( dtm, k ) {

  library(stm)

  out <- readCorpus( dtm, type = "slam" )

  documents <- out$documents
  vocab <- out$vocab

  topic <- stm(documents, vocab, K = k, init.type = "Spectral", max.em.its = 50)

  return( topic )

}
