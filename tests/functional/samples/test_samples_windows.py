# -*- coding: utf-8 -*-
# Copyright (C) 2019-2021 Intel Corporation
# SPDX-License-Identifier: Apache-2.0
import pytest

from utils.exceptions import FailedTestError


@pytest.mark.usefixtures('_is_image_os', '_is_distribution')
@pytest.mark.parametrize('_is_image_os', [('winserver2019', 'windows20h2')], indirect=True)
@pytest.mark.parametrize('_is_distribution', [('dev', 'proprietary')], indirect=True)
class TestSamplesWindows:
    @pytest.mark.xfail_log(pattern='Error: Download',
                           reason='Network problems when downloading alexnet files')
    def test_hello_classification_cpp_cpu(self, tester, image):
        kwargs = {'user': 'ContainerAdministrator'}
        tester.test_docker_image(
            image,
            ['cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'cd C:\\\\intel\\\\openvino\\\\samples\\\\cpp && '
             'C:\\\\intel\\\\openvino\\\\samples\\\\cpp\\\\build_samples_msvc.bat',
             'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\extras\\\\open_model_zoo\\\\tools\\\\'
             'model_tools\\\\downloader.py '
             '--name alexnet --precisions FP16 -o C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\'
             'Intel\\\\OpenVINO\\\\inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\',
             'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'cd C:\\\\intel\\\\openvino\\\\tools\\\\model_optimizer && '
             'python mo.py --output_dir C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\'
             'OpenVINO\\\\inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\public '
             '--input_model C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\public\\\\alexnet\\\\alexnet.caffemodel',
             'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\hello_classification '
             'C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\public\\\\alexnet.xml '
             'C:\\\\intel\\\\openvino\\\\samples\\\\scripts\\\\car_1.bmp CPU',
             ], self.test_hello_classification_cpp_cpu.__name__, **kwargs,
        )

    def test_hello_classification_cpp_fail(self, tester, image, caplog):
        kwargs = {'user': 'ContainerAdministrator'}
        with pytest.raises(FailedTestError):
            tester.test_docker_image(
                image,
                ['cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
                 'cd C:\\\\intel\\\\openvino\\\\samples\\\\cpp && '
                 'C:\\\\intel\\\\openvino\\\\samples\\\\cpp\\\\build_samples_msvc.bat',
                 'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
                 'python C:\\\\intel\\\\openvino\\\\extras\\\\open_model_zoo\\\\tools\\\\'
                 'model_tools\\\\downloader.py '
                 '--name vehicle-attributes-recognition-barrier-0039 --precisions FP16 '
                 '-o C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
                 'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\',
                 'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
                 'C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
                 'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\hello_classification '
                 'C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
                 'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\intel\\\\'
                 'vehicle-attributes-recognition-barrier-0039\\\\FP16\\\\'
                 'vehicle-attributes-recognition-barrier-0039.xml '
                 'C:\\\\intel\\\\openvino\\\\samples\\\\scripts\\\\car.png CPU',
                 ], self.test_hello_classification_cpp_fail.__name__, **kwargs,
            )
        if 'Sample supports models with 1 output only' not in caplog.text:
            pytest.fail('Sample supports models with 1 output only')

    def test_object_detection_cpp_cpu(self, tester, image):
        kwargs = {'user': 'ContainerAdministrator'}
        tester.test_docker_image(
            image,
            ['cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'cd C:\\\\intel\\\\openvino\\\\samples\\\\cpp && '
             'C:\\\\intel\\\\openvino\\\\samples\\\\cpp\\\\build_samples_msvc.bat',
             'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\extras\\\\open_model_zoo\\\\tools\\\\'
             'model_tools\\\\downloader.py '
             '--name vehicle-detection-adas-0002 --precisions FP16 '
             '-o C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\',
             'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\object_detection_sample_ssd '
             '-m C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\intel\\\\'
             'vehicle-detection-adas-0002\\\\FP16\\\\vehicle-detection-adas-0002.xml '
             '-i C:\\\\intel\\\\openvino\\\\samples\\\\scripts\\\\car_1.bmp -d CPU',
             ], self.test_object_detection_cpp_cpu.__name__, **kwargs,
        )

    @pytest.mark.xfail_log(pattern='Error: Download',
                           reason='Network problems when downloading alexnet files')
    def test_classification_async_cpp_cpu(self, tester, image):
        kwargs = {'user': 'ContainerAdministrator'}
        tester.test_docker_image(
            image,
            ['cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'cd C:\\\\intel\\\\openvino\\\\samples\\\\cpp && '
             'C:\\\\intel\\\\openvino\\\\samples\\\\cpp\\\\build_samples_msvc.bat',
             'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'python C:\\\\intel\\\\openvino\\\\extras\\\\open_model_zoo\\\\tools\\\\'
             'model_tools\\\\downloader.py '
             '--name alexnet --precisions FP16 -o C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\'
             'Intel\\\\OpenVINO\\\\inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\',
             'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'cd C:\\\\intel\\\\openvino\\\\tools\\\\model_optimizer && '
             'python mo.py --output_dir C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\'
             'OpenVINO\\\\inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\public '
             '--input_model C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\public\\\\alexnet\\\\alexnet.caffemodel',
             'cmd /S /C  C:\\\\intel\\\\openvino\\\\setupvars.bat && '
             'C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\classification_sample_async '
             '-m C:\\\\Users\\\\ContainerAdministrator\\\\Documents\\\\Intel\\\\OpenVINO\\\\'
             'inference_engine_cpp_samples_build\\\\intel64\\\\Release\\\\public\\\\alexnet.xml '
             '-i C:\\\\intel\\\\openvino\\\\samples\\\\scripts\\\\car_1.bmp -d CPU',
             ], self.test_classification_async_cpp_cpu.__name__, **kwargs,
        )
