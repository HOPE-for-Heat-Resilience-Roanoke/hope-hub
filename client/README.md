# Digital Hub
Digital Hub for the HOPE for Heat Resilience Project Frontend

Architecture based on [https://github.com/josean-dev/sveltekit-blog-walkthrough]()

## Steps to approve and show new things on the hub

Go to admin page and set the `approved` boolean flag on each new engagement to be added to the frontend.

```bash
./manage.py build_json > ../data/engagements_2024-07-17.json
cp ../data/engagements_2024-07-17.json ../client/static/engagements.json 
rsync -r --verbose --delete ~/hope-hub/server/hope_hub/media ~/hope-hub/client/static/images/engagements
cd ../client/
npm run build
sudo rsync -r --verbose --delete build/ /var/www/html
```

```
rsync -r --verbose --delete hope_hub/media ../client/static/images/engagements

rsync -r --verbose --delete ./hope_hub/media ../client/static/images/engagements

```