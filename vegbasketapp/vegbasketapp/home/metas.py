from meta.views import Meta


def get_vsmeta():
    vsmeta = Meta(
        title="Welcome to Veggie Sailor",
        description='Vegetarian Vegan Open Data Platform',
        keywords=['vegeterian','vegan', 'bar', 'restaurant'],
        image='https://veggiesailor.com/static/frontend/img/logo.png',
        url='https://veggiesailor.com',
        object_type='article',
        twitter_site='@veggiesailor',
        twitter_card='summary',
        use_og=True,
        user_twitter=True,
    )
    return vsmeta
