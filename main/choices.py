from django.utils.translation import ugettext_lazy as _


TEST_CHOICES = (
    ("Receiving",      _("Receiving")),
    ("Processing",     _("Processing")),
    ("Back Stocking",  _("Back Stocking")),
    ("Picking",        _("Report/Scan Picking")),
    ("Scanning",       _("Scanning Units")),
    ("LOAD",           _("Loading Truck")),
    ("DEL",            _("Delivering")),
    ("Break",          _("Break")),
    ("Cleaning",       _("Cleaning")),
    ("Lunch",          _("Lunch")),
)

STORE_CHOICES = (
    (116, _("116 - Orlando")),
    (167, _("167 - LBV")),
    (215, _("215 - Vineland")),
    (254, _("254 - Footwear")),
    (279, _("279 - Youth")),
    (517, _("517 - Disney")),
)
