#!/usr/bin/env bash
git remote rm origin
git remote add origin https://eindex:$GITHUB_API_KEY@github.com/eindex/github_trending_spider.git
git add -f .
git commit -m `date "+%F"`
git push -fq origin master > /dev/null
echo 'Done'