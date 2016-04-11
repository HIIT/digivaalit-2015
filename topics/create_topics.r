source('topics.r')

args <- commandArgs(trailingOnly = TRUE)

load( args[1] )
k <- as.integer( args[2] )

model <- create_model( dtm , k )

path <- paste( args[1] , '-', args[2], '.rdata' , sep = '' )
save( model , file = path )
