# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PerlEmailAbstract(PerlPackage):
    """Email::Abstract - unified interface to mail representations"""

    homepage = "https://metacpan.org/pod/Email::Abstract"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Abstract-3.009.tar.gz"

    maintainers("EbiArnie")

    version("3.009", sha256="040b7292e22e54815e9e6dfcdbfac9d874741930a20744ff5b369147dde201fc")

    depends_on("perl-email-simple", type=("build", "run"))
    depends_on("perl-mro-compat", type=("build", "run"))
    depends_on("perl-module-pluggable", type=("build", "run"))
