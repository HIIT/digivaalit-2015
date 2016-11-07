source('topics.r')

print( commandArgs(trailingOnly=TRUE) )

for( path in commandArgs(trailingOnly=TRUE) ) {

  df = data.frame( k = integer(), ll =integer() )

  for( f in list.files(path , pattern = '*.rdata') ){
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

  ## plot findings

  library('ggplot2')

  g <- ggplot( df , aes(k , ll ) ) +
  geom_line() +
  xlab('Aiheiden määrä') + ylab('Loglikelihood') +
  theme_minimal() +
  xlim(10,30)

  ggsave( file = 'plot.pdf' , g)

}
