source('topics.r')

print( commandArgs(trailingOnly=TRUE) )

for( path in commandArgs(trailingOnly=TRUE) ) {

  df = data.frame( k = integer(), ll =integer() )

  for( f in list.files(path) ){
  	load( paste(path, f, sep = '') )
  	k <- model@k
  	ll <- check_fitness_model( model )
  	row = c(k, ll)
  	df[ nrow(df)+1,] <- row
  }

  print("Examinging")
  print( path )

  print("Best fit k" )
  print( df$k[ which.max( df$ll ) ] )

  print("Best fit log likelihood")
  print( df$ll[ which.max( df$ll ) ] )
  print("") ## Empty line

}
