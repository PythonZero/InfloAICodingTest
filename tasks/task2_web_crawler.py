"""Task2:

Output a JSON file with the following contents:
    - [{ "url": input_url,
         "headline": web page's headline,
         "images": [{"url": image_url, "caption": caption},
                    {"url": image_url2, "caption": caption2)
                    ]
"""
import requests
import bs4
import json


class SingleScrape:

    def __init__(self, url):
        self.url = url
        self.content = self._get_url_content(url)
        self.soup = self._create_soup(self.content)
        self.headline = self._get_headline(self.soup)
        self.img_url_caption_list = self._get_images_and_captions(
            self.soup)
        self.output = self._prepare_output()

    @staticmethod
    def _get_url_content(url):
        """Get requests the url"""
        r = requests.get(url)
        return r.content

    @staticmethod
    def _create_soup(content):
        """Converts into beautiful soup object"""
        soup = bs4.BeautifulSoup(content, 'lxml')
        return soup

    @staticmethod
    def _get_headline(soup):
        """Gets the web page's headline"""
        return soup.title.string

    @classmethod
    def _get_images_and_captions(cls, soup):
        """
        :param soup:
        :return: list of {img_url: caption} dicts.
        Only return image if it has a caption.
        """
        image_url_caption_list = []
        figures = soup.findAll('figure')
        for figure in figures:

            img_url = cls._get_url_from_figure(figure)
            caption = cls._get_caption_from_figure(figure)

            if img_url and caption:
                image_url_caption_list.append(
                    {"url": img_url,
                     "caption": caption})

        return image_url_caption_list

    @staticmethod
    def _get_url_from_figure(figure, url_sources=('src', 'data-src')):
        """ :param figure: soup object of the figure
        :param url_sources: potential tags that contain the url
        :return: the first tag that contains the url,
                 or None if no matching tags found.
        """
        try:
            img = figure.find('img')
            img_url = [img[src] for src in url_sources if src in img.attrs]
            if img_url:
                return img_url[0]
        except (AttributeError, KeyError):
            return None

    @staticmethod
    def _get_caption_from_figure(figure):
        """Assume all text in figure is the caption.
        Should work for dirty websites"""
        return figure.text.replace("\n", "").strip()

    def _prepare_output(self):
        return {
            "url": self.url,
            "headline": self.headline,
            "images": self.img_url_caption_list
        }


class MultiScrape:
    def __init__(self, urls, output_path="task2.json"):
        self.urls = urls
        self.all_outputs = self._scrape_all_urls(self.urls)
        self.json_out = self._jsonify_out(self.all_outputs)
        self.save_output(self.json_out, output_path)

    @staticmethod
    def _scrape_all_urls(urls):
        all_outputs = []
        for url in urls:
            single_output = SingleScrape(url).output
            all_outputs.append(single_output)
        return all_outputs

    @staticmethod
    def _jsonify_out(all_outputs, indent=4):
        return json.dumps(all_outputs, indent=indent)

    @staticmethod
    def save_output(content, output_path):
        with open(output_path, "w+") as f:
            f.write(content)

if __name__ == '__main__':
    url = "https://www.skysports.com/football/news/11661/10871659/who-won-your-clubs-player-of-the-year-award"
    scraper1 = SingleScrape(url)
    url2 = "https://www.bbc.co.uk/sport/tennis/37268846"
    scraper2 = SingleScrape(url2)

    urls = [url, url2]
    MultiScrape(urls)
