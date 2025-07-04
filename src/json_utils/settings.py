import json
import functools

@functools.lru_cache
def get_data_from_json() -> str:
    with open("json_utils/data.json","r") as file:
            data = json.load(file)
            
            manga_name = data["manga_data"]["manga_title"]
            button_color = data["settings"]["button_color"]
            button_hover_color = data["settings"]["button_hover_color"]
            color_blue = data["settings"]["color_blue"]
            block_color = data["settings"]["block_color"]
            color_green = data["settings"]["color_green"]
            history = data["user_var"][f"{manga_name}"]
            len_history = data["user_var"]
            text_color = data["settings"]["text_color"]
            colorscheme = data["settings"]["colorscheme"]   

            dark_charcoal = data["settings"]["dark charcoal"]
            electric_blue = data["settings"]["electric Blue"]
            background = data["settings"]["background"]
            font_size = data["settings"]["font_size"]
            manga_location = data["settings"]["manga_location"]
            chapter_download = data["settings"]["chapter_download"]

            mangas_downloaded = data["user_var"]


            return button_color,button_hover_color,block_color,color_blue,color_green,history,manga_name,len_history,dark_charcoal,electric_blue,background,font_size,manga_location,chapter_download,text_color,colorscheme,mangas_downloaded
            
button_color,button_hover_color,block_color,color_blue,color_green,history,manga_name,len_history,dark_charcoal,electric_blue,background,font_size,manga_location,chapter_download,text_color,colorscheme,mangas_downloaded = get_data_from_json()
