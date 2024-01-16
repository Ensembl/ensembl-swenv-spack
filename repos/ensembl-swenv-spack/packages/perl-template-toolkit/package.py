# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PerlTemplateToolkit(PerlPackage):
    """Template - Front-end module to the Template Toolkit"""

    homepage = "https://metacpan.org/pod/Template"
    url = "https://cpan.metacpan.org/authors/id/A/AB/ABW/Template-Toolkit-3.101.tar.gz"

    maintainers("EbiArnie")

    version("3.101", sha256="d2a32dd6c21e4b37c6a93df8087ca9e880cfae613a3e5efaea307b0bdcaedb58")

    depends_on("perl-pathtools", type=("build", "run"))
    depends_on("perl-appconfig", type=("build", "run"))

    def configure_args(self):
        return [
            'TT_XS_DEFAULT=y',
            'TT_ACCEPT=y'
        ]
