#!/usr/bin/env bash
git remote rm origin
git remote add origin https://eindex:$GITHUB_API_KEY@github.com/eindex/github_trending_spider.git
git add .
git commit -m `date "+%F"`
git push -u origin master
echo 'Done'