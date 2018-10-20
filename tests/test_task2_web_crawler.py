import json
import os

import bs4
import pytest

from tasks.task2_web_crawler import SingleScrape, MultiScrape


@pytest.fixture('module')
def sample_html():
    """opens the sample_html file"""
    with open(os.path.join(
            os.path.dirname(__file__), 'sample_html.html'
    ), encoding='utf8') as f:
        content = f.read()

    return content


@pytest.fixture('module')
def soup(sample_html):
    return SingleScrape._create_soup(sample_html)


def test_get_url():
    url = "https://www.skysports.com/football/news/11661/10871659/who-won-your-clubs-player-of-the-year-award"
    assert b'skysports' in SingleScrape._get_url_content(url)


def test_create_soup(soup):
    assert issubclass(type(soup),
                      bs4.BeautifulSoup)
    assert 'html' == soup.contents[0]


def test_get_headline(soup):
    title = SingleScrape._get_headline(soup)
    assert title == r"Who won your club's Player of the Year award? | Football News | Sky Sports"


def test_get_url_from_figure(soup):
    figure = soup.find('figure')  # get the first figure
    img_url = SingleScrape._get_url_from_figure(figure)
    assert img_url == r"https://e1.365dm.com/17/04/768x432/" \
                      r"skysports-ngolo-kante-chelsea-pfa-award_3937274.jpg?20170423234739"


def test_get_url_from_figure_no_imgs():
    figure = bs4.BeautifulSoup("<p> hello </p>")
    img_url = SingleScrape._get_url_from_figure(figure)
    assert img_url is None


def test_get_caption_from_figure(soup):
    figure = soup.find('figure')  # get the first figure
    caption = SingleScrape._get_caption_from_figure(figure)
    assert caption == r"N'Golo Kante with the PFA Players' Player of the Year award"


# TODO: write caption test for BBC (no time)

def test_get_images_and_captions(soup):
    img_url_cpns = SingleScrape._get_images_and_captions(soup)
    assert {"url": r"https://e1.365dm.com/17/04/768x432/"
                   r"skysports-ngolo-kante-chelsea-pfa-award"
                   r"_3937274.jpg?20170423234739",
            "caption": r"N'Golo Kante with the PFA Players' Player of the Year award"
            } in img_url_cpns


def test_prepare_output():
    mock_scrape = SingleScrape.__new__(SingleScrape)
    mock_scrape.url = "http://infloAI.ai"
    mock_scrape.headline = "infloAI"
    mock_scrape.img_url_caption_list = [
        {"/img1.png": 'default img1'},
        {"/img2.png": 'the second image'}
    ]
    output = mock_scrape._prepare_output()
    expected_out = {"url": "http://infloAI.ai",
                    "headline": "infloAI",
                    "images": [
                        {"/img1.png": 'default img1'},
                        {"/img2.png": 'the second image'}]}

    assert expected_out == output


def test_multi_scrape_json():
    all_outputs = [
        {"url": "http://infloAI.ai",
         "headline": "infloAI",
         "images": [
             {"/img1.png": 'default img1'},
             {"/img2.png": 'the second image'}]},

        {"url": "http://google.com",
         "headline": "Google",
         "images": [
             {"/img3.png": "google homepage"},
             ]}
    ]
    json_out = MultiScrape._jsonify_out(all_outputs, indent=0)
    assert json_out.replace("\n", "") == """[{"url": "http://infloAI.ai","headline": "infloAI","images": 
    [{"/img1.png": "default img1"},{"/img2.png": "the second image"}]},{"url": "http://google.com","headline": 
    "Google","images": [{"/img3.png": "google homepage"}]}]"""

