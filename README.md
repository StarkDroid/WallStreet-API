# WallStreet-API

## This repository serves as a static API to access all the wallpapers that can be seen in the [WallStreet app](https://github.com/StarkDroid/WallStreet). I would love to see your favourite wallpapers being added here!

> [!IMPORTANT]
> Please read the below pointers before proceeding with contributions.

🔹Contributed wallpapers should not be from any copyright sources.

🔹Try not to spam the pull request, instead dump all your collection at once or squash the commits

🔹Submission of images with obscenity, political or controversial content will be banished immediately.

# How to Contribute?

1. Fork this repository and clone it in your machine. Make sure you have latest commits.
2. Add your images into `wallpapers` folder (Make sure not to have duplicate naming)
3. Portrait images (specifically for mobile) needs to be added inside `mobile/thumbnail/` directory, landscape images (for desktop) needs to be added inside `desktop/thumbnail`
4. Add a new individual JSON object block for every wallpaper you add at the end of `wallstreet_walls.json`,
> Here's the JSON Schema to follow
```
{
  "category": "#categoryName",
  "imageUrl": "https://raw.githubusercontent.com/StarkDroid/WallStreet-API/main/wallpapers/your_wallpaper_name.png",
  "thumbnailUrl": "<base_url>/desktop (or) mobile/thumbnail/<file_name>.png"
}
```
> [!IMPORTANT]
> The App is capable of handing formats like `JPG`, `PNG` and `PNG`

1. Once done `git add . && git commit -m "Add your desired commit message" && git push origin gh-pages`.
2. Then finally head to git and make a pull request to the original `WallStreet-API` repository.