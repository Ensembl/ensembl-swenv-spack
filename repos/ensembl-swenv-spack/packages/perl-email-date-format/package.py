# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PerlEmailDateFormat(PerlPackage):
    """Email::Date::Format - produce RFC 2822 date strings"""

    homepage = "https://metacpan.org/pod/Email::Date::Format"
    url = "https://cpan.metacpan.org/authors/id/R/RJ/RJBS/Email-Date-Format-1.008.tar.gz"

    maintainers("EbiArnie")

    version("1.008", sha256="432b7c83ff88749af128003f5257c573aec1a463418db90ed22843cbbc258b4f")
