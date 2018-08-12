#!/bin/bash -x

type gem
type bundle

bundle exec gem list quality

if bundle exec gem list quality -i >/dev/null 2>&1
then
  if [ -f Rakefile.quality ]
  then
    rake -f Rakefile.quality quality
  else
    rake quality
  fi
else
  if [ -f Rakefile.quality ]
  then
    docker run -v "$(pwd)":/usr/app -v "$(pwd)"/Rakefile.quality:/usr/quality/Rakefile apiology/quality:jumbo-latest
  else
    docker run -v "$(pwd):/usr/app" apiology/quality:jumbo-latest "$@"
  fi
fi
