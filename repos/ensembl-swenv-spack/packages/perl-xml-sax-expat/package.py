# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlXmlSaxExpat(PerlPackage):
    """SAX Driver for Expat"""

    homepage = "https://metacpan.org/pod/XML::SAX::Expat"
    url = "https://cpan.metacpan.org/authors/id/B/BJ/BJOERN/XML-SAX-Expat-0.51.tar.gz"

    maintainers("EbiArnie")

    version("0.51", sha256="4c016213d0ce7db2c494e30086b59917b302db8c292dcd21f39deebd9780c83f")

    depends_on("perl-xml-namespacesupport@0.03:", type=("run"))
    depends_on("perl-xml-parser@2.27:", type=("run"))
    depends_on("perl-xml-sax@0.03:", type=("run"))
    depends_on("perl-xml-sax-base@1.00:", type=("run"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
