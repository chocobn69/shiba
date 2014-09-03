__author__ = "boguta_m"

from .. import shiba


class MarketplaceManagement(shiba.Shiba):
    """ Marketplace informations retrieving, such as product lists and category mapping"""

    def __init__(self, login, pwd, version, mode=""):
        super(MarketplaceManagement, self).__init__(login, pwd, version, mode)

    def get_product_list(self, scope="", kw="", nav="", refs="", productids="", ppp=20, pnumber=1):
        """Prints a list from given parameters.

        :param scope: None (classic results), "PRICING" (classic results plus 10 best announces)
        or "LIMITED" (search in categories in which rapid put on sale is possible through WS)
        :param kw: Research keyword
        :param nav: Navigation category (url friendly ones, can be found on PriceMinister categories' URLs)
        :param refs: EAN, or ISBN, even as a list.
        :param productids: Same as refs but as products ID.
        :param ppp: Products per page, default is 20.
        :param pnumber: Page number, default is 1.
        """

        assert(type(refs) is not list or str or type(productids) is not list or str,
               "error : bad type given as refs or productids")
        reflist = ','.join(refs)
        plist = ','.join(productids)
        if len(scope) != 0 and scope != "PRICING" and scope != "LIMITED":
            scope = ""
        if int(ppp) <= 0:
            ppp = 20
        if int(pnumber) <= 0:
            pnumber = 1
        url = self.url + "action=listing" \
            + "&login=" + self.login \
            + "&version=" + self.version
        if len(scope) > 0:
            url += "&scope=" + str(scope)
        if len(kw) > 0:
            url += "&kw=" + str(kw)
        if len(nav) > 0:
            url += "&nav=" + str(nav)
        if len(refs) > 0:
            url += "&refs="
            url += refs if type(refs) != list else reflist
        if len(productids) > 0:
            url += "&productids="
            url += productids if type(refs) != list else plist
        url += "&nbproductsperpage=" + str(ppp) \
            + "&pagenumber=" + str(pnumber)
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/listing")
        return dictionary

    def get_category_map(self):
        url = self.url + "action=categorymap" \
            + "&login=" + self.login \
            + "&version=" + self.version
        dictionary = self.__retrieve_dict_from_url(url, "http://www.priceminister.com/sales_ws/listing")
        return dictionary