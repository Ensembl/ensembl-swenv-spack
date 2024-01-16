# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlJsonMaybexs(PerlPackage):
    """Use Cpanel::JSON::XS with a fallback to JSON::XS and JSON::PP"""

    homepage = "https://metacpan.org/pod/JSON::MaybeXS"
    url = "https://cpan.metacpan.org/authors/id/E/ET/ETHER/JSON-MaybeXS-1.004005.tar.gz"

    maintainers("EbiArnie")

    version("1.004005", sha256="f5b6bc19f579e66b7299f8748b8ac3e171936dc4e7fcb72a8a257a9bd482a331")

    depends_on("perl@5.6.0:", type=("build", "link", "run", "test"))
    depends_on("perl-test-needs@0.002006:", type=("test"))

    # FIXME: Add all non-perl dependencies and cross-check with the actual
    # package build mechanism (e.g. Makefile.PL)

    def configure_args(self):
        # FIXME: Add non-standard arguments
        # FIXME: If not needed delete this function
        args = []
        return args
