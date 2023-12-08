# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlBioDbHts(PerlPackage):
    """Perl interface to HTS library for DNA sequencing"""

    homepage = "https://metacpan.org/pod/Bio::DB::HTS"
    url = "https://cpan.metacpan.org/authors/id/A/AV/AVULLO/Bio-DB-HTS-3.01.tar.gz"

    maintainers("EbiArnie")

    version("3.01", sha256="12a6bc1f579513cac8b9167cce4e363655cc8eba26b7d9fe1170dfe95e044f42")

    depends_on("perl@5.8.0:", type=("build", "link", "run", "test"))
    depends_on("htslib", type=("build", "link", "run"))
    depends_on("perl-bioperl", type=("run"))

    def configure_args(self):
        args = ['--htslib', self.spec["htslib"].prefix.lib ]
        return args
