source('topics.r')

for( path in commandArgs(trailingOnly=TRUE) ) {

   print( paste( "Working on" , path ) )

   unlink( paste( path , '*.rdata*', sep = '' ) ) ## remove all existing rdata in the folder

   dtm <- create_dtm( path )
   save( dtm , file = paste( path, 'dtm.rdata' , sep = '' ) )

}
