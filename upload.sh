#!/usr/bin/env bash
git remote rm origin
git remote add origin
git add -f .
git commit -m `date "+%F"`
git -c user.name='travis' -c user.email='travis' commit -m init
git push -f -q https://eindex:$GITHUB_API_KEY@github.com/eindex/github_trending_spider.git master &2>/dev/null
echo 'Done'