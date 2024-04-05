# WallStreet-API

## This repository serves as a static API to access all the wallpapers that can be seen in the [WallStreet app](https://github.com/StarkDroid/WallStreet). I would love to see your favourite wallpapers being added here!

> [!IMPORTANT]
> Please read the below pointers before proceeding with contributions.

🔹Contributed wallpapers should not be from any copyright sources.

🔹Try to stick to AI generated wallpapers for a more unique collection.

🔹Try not to spam the pull request, instead dump all your collection at once or squash and the commits

🔹Submission of images with obscenity, political or controversial content will be banished immediately.

# How to Contribute?

1. Fork this repository and clone it in your machine. Make sure you have latest commits.
2. Add your images into `wallpapers` folder (Make sure not to have duplicate naming)
3. Add a new individual JSON object block for every wallpaper you add at the end of `wallstreet_walls.json`,
> Here's the JSON Schema to follow
```
{
  "wallpaper_name": "Enter the wallpaper name here",
  "author": "Your name or whoever created the wallpaper",
  "imageUrl": "https://raw.githubusercontent.com/StarkDroid/WallStreet-API/main/wallpapers/your_wallpaper_name.png",
  "imageUrlHD": "Same as imageUrl but point to the Upscaled image"
}
```
> [!IMPORTANT]
> If the file size is large, Try not to include it in imageURL, instead use imageUrlHD, As then imageURL can be used to show the thumbnail of your wallpaper while the imageUrlHD can be used to download the upscaled wallpaper.

4. Once done `git add . && git commit -m "Add your desired commit message" && git push origin main`.
5. Then finally head to git and make a pull request to the original `WallStreet-API` repository.