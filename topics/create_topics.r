source('topics.r')
##source('stm.r')

args <- commandArgs(trailingOnly = TRUE)

print( args[1] )

load( paste( args[1] , 'dtm.rdata', sep='' ) )
k <- as.integer( args[2] )

model <- create_model( dtm , k )

path <- paste( args[1] , '/topic-', args[2], '.rdata' , sep = '' )
save( model , file = path )
