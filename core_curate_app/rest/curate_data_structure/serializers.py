"""Curate Data Structure Serializers
"""

from rest_framework_mongoengine.serializers import DocumentSerializer

from core_curate_app.components.curate_data_structure import (
    api as curate_data_structure_api,
)
from core_curate_app.components.curate_data_structure.models import CurateDataStructure


class CurateDataStructureSerializer(DocumentSerializer):
    """CurateDataStructure Serializer"""

    class Meta(object):
        """Meta"""

        model = CurateDataStructure
        fields = "__all__"

    def create(self, validated_data):
        """
        Create and return a new `CurateDataStructure` instance, given the validated data.
        """
        # Create data
        curate_data_structure = CurateDataStructure(
            name=validated_data["name"],
            template=validated_data["template"],
            form_string=validated_data["form_string"]
            if "form_string" in validated_data
            else None,
            user=str(validated_data["user_request"].id),
            data=validated_data["data"] if "data" in validated_data else None,
            data_structure_element_root=validated_data["data_structure_element_root"]
            if "data_structure_element_root" in validated_data
            else None,
        )

        return curate_data_structure_api.upsert(
            curate_data_structure, validated_data["user_request"]
        )

    def update(self, instance, validated_data):
        """
        Update and return an existing `CurateDataStructure` instance, given the validated data.
        """
        instance.name = validated_data.get("name", instance.name)
        instance.form_string = validated_data.get("form_string", instance.form_string)
        instance.data_structure_element_root = validated_data.get(
            "data_structure_element_root", instance.data_structure_element_root
        )
        instance.data = validated_data.get("data", instance.data)

        return curate_data_structure_api.upsert(
            instance, validated_data["user_request"]
        )