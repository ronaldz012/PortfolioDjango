# apps/core/models.py
from django.db import models
from django.utils.text import slugify

################################################################################################
class Technology(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    icon = models.CharField(
        max_length=50, 
        blank=True, 
        help_text="Icon name (e.g., react, python, django)"
    )
    
    class Meta:
        verbose_name = "Technology"
        verbose_name_plural = "Technologies"
    
    def __str__(self):
        return self.name
###############################################################################################
# apps/core/models.py
from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language # Necesario para las properties

# ... (El modelo Technology va arriba)

class Project(models.Model):
    # --- Campos Básicos y URL ---
    slug = models.SlugField(unique=True, blank=True, verbose_name="Friendly URL")
    
    # --- Campos de Contenido (Inglés por defecto) ---
    title = models.CharField(max_length=200, verbose_name="Title")
    short_description = models.CharField(
        max_length=300, 
        verbose_name="Short description",
        help_text="Shown in project cards"
    )
    # Cuerpo principal del proyecto, acepta contenido HTML
    body_html = models.TextField(
        verbose_name="Body Content (HTML)",
        help_text="Full project content using HTML",
    )
    
    # --- Campos de Contenido (Español) ---
    title_es = models.CharField(max_length=200, verbose_name="Título (Español)")
    short_description_es = models.CharField(
        max_length=300, 
        verbose_name="Descripción corta (Español)",
        help_text="Se muestra en las tarjetas de proyecto"
    )
    # Cuerpo principal en español
    body_html_es = models.TextField(
        verbose_name="Cuerpo del contenido (HTML Español)",
        help_text="Contenido completo del proyecto usando HTML",
    )
    
    # --- Metadata y Relaciones ---
    technologies = models.ManyToManyField(
        Technology, 
        related_name='projects', 
        verbose_name="Technologies",
        blank=True
    )
    github_url = models.URLField(blank=False, default='', verbose_name="GitHub URL")
    video_url = models.URLField(blank=True, default='', verbose_name="Video URL")
    demo_url = models.URLField(blank=True,default='', verbose_name="Demo URL")
    featured = models.BooleanField(default=False, verbose_name="Featured")
    order = models.IntegerField(default=0, verbose_name="Order")
    
    # --- Clases Internas y Métodos ---
    class Meta:
        ordering = ['order', '-id']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title # Muestra el título en inglés en el Admin
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title) # Crea slug basado en el título en inglés
        super().save(*args, **kwargs)
        
    # --- Propiedades Inteligentes para Traducción ---
    @property
    def get_title(self):
        """Devuelve el título según el idioma activo (Inglés por defecto)."""
        lang = get_language()
        return getattr(self, f'title_{lang}', self.title)
    
    @property
    def get_short_description(self):
        """Devuelve la descripción corta según el idioma activo (Inglés por defecto)."""
        lang = get_language()
        return getattr(self, f'short_description_{lang}', self.short_description)
    
    @property
    def get_body_html(self):
        """Devuelve el cuerpo del proyecto (HTML) según el idioma activo (Inglés por defecto)."""
        lang = get_language()
        return getattr(self, f'body_html_{lang}', self.body_html)