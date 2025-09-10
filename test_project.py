from categories import build_product_url

def test_build_product_url_basic():
    url, slug = build_product_url("Mobiles", 1)
    assert url == "https://priceoye.pk/mobiles?page=1"
    assert slug == "mobiles"

def test_build_product_url_special_case():
    url, slug = build_product_url("TV & Home Appliances", 1)
    assert "tv-home-appliances" in slug
    assert url.startswith("https://priceoye.pk/")
