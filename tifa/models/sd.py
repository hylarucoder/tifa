from django.db import models

from tifa.models.base import Model


class SdModelCheckpoint(Model):
    class Meta:
        db_table = "sd_model_checkpoint"

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    sort_num = models.IntegerField(db_index=True, default=999)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


class SdModelVae(Model):
    class Meta:
        db_table = "sd_model_vae"

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    sort_num = models.IntegerField(db_index=True, default=999)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


class SdModelLora(Model):
    class Meta:
        db_table = "sd_model_lora"

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    sort_num = models.IntegerField(db_index=True, default=999)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)


class SdPromptTag(Model):
    class Meta:
        db_table = "sd_prompt_tag"

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100)
    name_zh = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, unique=True)
    sort_num = models.IntegerField(db_index=True, default=999)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<#{self.id}> - {self.name}|{self.name_zh}"


class SdSpellTemplate(Model):
    class Meta:
        db_table = "sd_spell_template"

    id = models.BigAutoField(primary_key=True)
    slug = models.CharField(max_length=100)
    checkpoint = models.CharField(max_length=100)
    prompt = models.TextField()
    n_prompt = models.TextField()
    sampler = models.CharField(max_length=50)
    cfg_scale = models.IntegerField(default=7)
    steps = models.IntegerField(default=30)
    seed = models.BigIntegerField(default=-1)
    sort_num = models.IntegerField(db_index=True, default=999)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<#{self.id}> - {self.prompt}"


class SdPrompt(Model):
    class Meta:
        db_table = "sd_prompt"

    id = models.BigAutoField(primary_key=True)
    checkpoint = models.CharField(max_length=100)
    template_slug = models.CharField(max_length=100)
    prompt = models.TextField()
    n_prompt = models.TextField()
    sampler = models.CharField(max_length=50)
    cfg_scale = models.IntegerField(default=7)
    steps = models.IntegerField(default=30)
    seed = models.BigIntegerField(default=-1)
    sort_num = models.IntegerField(db_index=True, default=999)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<#{self.id}> - {self.name}"


class SdImage(Model):
    class Meta:
        db_table = "sd_image"

    id = models.BigAutoField(primary_key=True)
    sort_num = models.IntegerField(db_index=True, default=999)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"<#{self.id}> - {self.sort_num}"
