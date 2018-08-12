#!/bin/bash -x

if ! bundle exec gem list quality -i >/dev/null 2>&1
then
  bundle install
fi

if [ -f Rakefile.quality ]
then
  bundle exec rake -f Rakefile.quality quality
else
  bundle exec rake quality
fi
