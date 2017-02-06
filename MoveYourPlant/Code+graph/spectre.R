library(seewave)
library(tuneR)

dir <- c(list.files(path = ".", pattern = ".wav"))

for (i in dir){
  s <- readWave(i)
  spec <- meanspec(s, from=30, plot=FALSE)
  fpeaks(spec)
  freq <- fpeaks(spec, nmax=1)
  cat(i, ' ', freq[1], ',', sep='')
}

