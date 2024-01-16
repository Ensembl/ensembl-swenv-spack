# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PerlEmailSender(PerlPackage):
    """Email::Sender::Simple - the simple interface for sending mail with Sender"""

    homepage = "https://metacpan.org/pod/Email::Sender::Simple"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Sender-2.600.tar.gz"

    maintainers("EbiArnie")

    version("2.600", sha256="ecc675d030d79d9a4fb064567ea885c66b17c3862379ad30f8205a281cd8ee29")

    depends_on("perl-email-abstract", type=("build", "run"))
    depends_on("perl-email-address-xs", type=("build", "run"))
    depends_on("perl-email-simple", type=("build", "run"))
    depends_on("perl-module-runtime", type=("build", "run"))
    depends_on("perl-moo", type=("build", "run"))
    depends_on("perl-moox-types-mooselike", type=("build", "run"))
    depends_on("perl-sub-exporter", type=("build", "run"))
    depends_on("perl-throwable", type=("build", "run"))
    depends_on("perl-try-tiny", type=("build", "run"))
    depends_on("perl-capture-tiny", type=("test"))

