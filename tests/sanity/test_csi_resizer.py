#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

import pytest
from k8s_test_harness.util import docker_util, env_util


@pytest.mark.parametrize("image_version", ("1.10.1", "1.11.1"))
def test_csi_resizer_rock(image_version):
    """Test csi-resizer rock."""
    rock = env_util.get_build_meta_info_for_rock_version(
        "csi-resizer", image_version, "amd64"
    )
    image = rock.image

    # check binary.
    process = docker_util.run_in_docker(image, ["/csi-resizer", "--help"])
    assert "Usage of /csi-resizer" in process.stderr
