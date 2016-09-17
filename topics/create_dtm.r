source('~/digivaalit_public/topics/topics.r')

paths <- c( 'citizen-tweets-lemma' , 'digivaalit-media-lemmas', 'candidate-tweets-lemma' )

for( path in paths ) {

   path = paste( '/homeappl/home/mnelimar/' , path, '/',  sep = '' )

   print( paste( "Working on" , path ) )

   unlink( paste( path , '*.rdata*', sep = '' ) )
   dtm <- create_dtm( path )
   save( dtm , file = paste( path, 'dtm.rdata' , sep = '' ) )

}
