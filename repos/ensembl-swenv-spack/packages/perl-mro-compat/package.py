# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PerlMroCompat(PerlPackage):
    """MRO::Compat - mro::* interface compatibility for Perls < 5.9.5"""

    homepage = "https://metacpan.org/pod/MRO::Compat"
    url = "https://cpan.metacpan.org/authors/id/H/HA/HAARG/MRO-Compat-0.15.tar.gz"

    maintainers("EbiArnie")

    version("0.15", sha256="0d4535f88e43babd84ab604866215fc4d04398bd4db7b21852d4a31b1c15ef61")
