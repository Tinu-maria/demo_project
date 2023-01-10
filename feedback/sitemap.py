from django.contrib.sitemaps import Sitemap
from django.shortcuts import reverse


class SitemapView(Sitemap):
    priority = 0.8
    protocol = 'http'
    changefreq = "weekly"

    def items(self):
        return ['cache']

    def location(self, item):
        return reverse(item)
