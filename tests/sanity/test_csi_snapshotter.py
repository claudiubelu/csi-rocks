#
# Copyright 2024 Canonical, Ltd.
# See LICENSE file for licensing details
#

from k8s_test_harness.util import docker_util, env_util

ROCK_EXPECTED_FILES = [
    "/bin/pebble",
]


def test_csi_snapshotter_rock():
    """Test csi-snapshotter rock."""
    rock = env_util.get_build_meta_info_for_rock_version(
        "csi-snapshotter", "6.3.3", "amd64"
    )
    image = rock.image

    # check rock filesystem.
    docker_util.ensure_image_contains_paths(image, ROCK_EXPECTED_FILES)
