# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)
from spack.package import *


class PyCactus(PythonPackage):
    """Cactus is a reference-free whole-genome alignment program, as well as a pagenome graph construction toolkit."""

    homepage = "https://github.com/ComparativeGenomicsToolkit/cactus"

    url = "https://github.com/ComparativeGenomicsToolkit/cactus/archive/refs/tags/v2.6.4.tar.gz"

    maintainers("EbiArnie")

    version("2.6.4", sha256="647342cd1289c2ee6e230194e37e23b7fce03855fdb3f99d3d1f35130010ae99")

    depends_on("py-setuptools", type="build")

    depends_on("py-decorator", type=("build", "run"))
    depends_on("py-networkx@2:2.8.2", type=("build", "run"))
    depends_on("py-pytest", type=("build", "run"))
    depends_on("py-cigar", type=("build", "run"))
    depends_on("py-biopython", type=("build", "run"))

    depends_on("bedtools2@2.30.0", type=("build", "link", "run"))
    depends_on("samtools@1.11", type=("build", "link", "run"))
    depends_on("mash@2.3", type=("build", "link", "run"))

#    phast@ gitrel=85f7ed179dd097a86ba4added22d571785cc3e1d , built with clapack321
# TODO: include gitref with phast

#    kent@415
# TODO - add version to pkg

#    - minimap2 @ 2.21
# TODO add version or test newer versions

# - minigraph @0.20
# TODO https://github.com/lh3/minigraph

# - gfatools @0.5
# TODO https://github.com/lh3/gfatools

# - dna-brnn  # /lh3/dna-nn.git, @ git 2e6d242ae339457b985f50086e85194c3ce418b1
# TODO

# - cactus-gfa-tools @ git 9b26caa961d6e72ad3747e5c2ce81cdf1e9b63c3
# https://github.com/ComparativeGenomicsToolkit/cactus-gfa-tools
# TODO

# The following tools are included to export and work with pangenome graph formats
# - hal2vg @ 1.1.2
# https://github.com/ComparativeGenomicsToolkit/hal2vg
# TODO

# - vg @1.49.0 (vgteam/vg)
# TODO

# maf_stream@0.1
# https://github.com/joelarmstrong/maf_stream
# TODO

# maftools @ gitref 837b8f27c7bf781c7cbee3972b94e91aa6a77790
# https://github.com/dentearl/mafTools
# TODO

# taffy @ git c75ce895b7975e7ac17cb1ce964db3016615de47
# ComparativeGenomicsToolkit/taffy.git
# TODO

# sonlib @ git 9734083dffb180e3d76c323609c082b401336c0a
# TODO - add version to pkg

# marschall-lab/GFAffix, @0.1.4b
# TODO

# pangenome/vcfbub @0.1.0
# TODO

# pangenome/odgi @0.8.3
# TODO

# probably not needed directly: htslib @1.11 # is there in any case


    def global_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py
        # FIXME: If not needed, delete this function
        options = []
        return options

    def install_options(self, spec, prefix):
        # FIXME: Add options to pass to setup.py install
        # FIXME: If not needed, delete this function
        options = []
        return options
