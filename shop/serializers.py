from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name',)

# class ArtistDetailSerializer(ArtistSerializer):
#     musics = MusicSerializer(source="music_set", many=True)
#     musics_count = serializers.IntegerField(source='music_set.count')
    
#     class Meta(ArtistSerializer.Meta):
#         fields = ArtistSerializer.Meta.fields + ('musics', 'musics_count',) 