source('topics.r')

df = data.frame( k = integer(), ll =integer() )

for( path in commandArgs(trailingOnly=TRUE) ) {

  for( f in list.files(path) ){
  	load( paste(path, f, sep = '') )
  	k <- model@k
  	ll <- check_fitness_model( model )
  	row = c(k, ll)
  	df[ nrow(df)+1,] <- row
  }

  print("Examinging", path )
  print("Best fit log likelihood", which.max( df$ll ) )
  print("Best fit k", df$k[ which.max( df$ll ) ] )
  print("") ## Empty line

}
