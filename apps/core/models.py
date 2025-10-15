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
class Skill(models.Model):   
    # Campo base (Inglés)
    name = models.CharField(
        max_length=50, 
        verbose_name="Category Name (English)"
    )
    
    # Campo de traducción (Español)
    name_es = models.CharField(
        max_length=50, 
        verbose_name="Nombre de Categoría (Español)"
    )
    
    class Meta:
        verbose_name = "Skill"
        verbose_name_plural = "Skills"
    def __str__(self):
        return self.name

    @property
    def get_name(self):
        lang = get_language()
        return getattr(self, f'name_{lang}', self.name)
###############################################################################################
# apps/core/models.py
from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language # Necesario para las properties

# ... (El modelo Technology va arriba)

from django.db import models
from django.utils.text import slugify
from django.utils.translation import get_language


class Project(models.Model):
    # ===========================================
    # IDENTIFICACIÓN Y URL
    # ===========================================
    slug = models.SlugField(
        unique=True, 
        blank=False, 
        verbose_name="Friendly URL"
    )
    
    # ===========================================
    # CONTENIDO PRINCIPAL - INGLÉS
    # ===========================================
    title = models.CharField(
        max_length=200, 
        verbose_name="Title"
    )
    short_description = models.CharField(
        max_length=300,
        verbose_name="Short description",
        help_text="Shown in project cards (listing view)"
    )
    
    # Dividido en 3 secciones para intercalar imágenes
    body_html_intro = models.TextField(
        verbose_name="Introduction (HTML)",
        help_text="First section - Overview, problem statement, context",
        blank=True
    )
    
    body_html_middle = models.TextField(
        verbose_name="Middle Content (HTML)",
        help_text="Second section - Solution, implementation, technical details",
        blank=True
    )
    
    body_html_conclusion = models.TextField(
        verbose_name="Conclusion (HTML)",
        help_text="Final section - Results, learnings, future improvements",
        blank=True
    )
    
    # ===========================================
    # CONTENIDO PRINCIPAL - ESPAÑOL
    # ===========================================
    title_es = models.CharField(
        max_length=200, 
        verbose_name="Título (Español)"
    )
    short_description_es = models.CharField(
        max_length=300,
        verbose_name="Descripción corta (Español)",
        help_text="Se muestra en las tarjetas de proyecto (vista de listado)"
    )
    
    body_html_intro_es = models.TextField(
        verbose_name="Introducción (HTML Español)",
        help_text="Primera sección - Resumen, problema, contexto",
        blank=True
    )
    
    body_html_middle_es = models.TextField(
        verbose_name="Contenido Medio (HTML Español)",
        help_text="Segunda sección - Solución, implementación, detalles técnicos",
        blank=True
    )
    
    body_html_conclusion_es = models.TextField(
        verbose_name="Conclusión (HTML Español)",
        help_text="Sección final - Resultados, aprendizajes, mejoras futuras",
        blank=True
    )
    
    # ===========================================
    # IMÁGENES Y MULTIMEDIA
    # ===========================================
    # Para listing/cards
    thumbnail = models.ImageField(
        upload_to='projects/thumbnails/',
        verbose_name="Miniatura",
        help_text="Imagen para tarjeta en listado (Recomendado: 800x600px)",
        blank=True,
        null=True
    )
    
    # Imágenes para intercalar en el contenido de detalle
    image_after_intro = models.ImageField(
        upload_to='projects/content/',
        verbose_name="Imagen después de Intro",
        help_text="Se muestra entre intro y middle section (ej: diagrama de arquitectura)",
        blank=True,
        null=True
    )
    
    image_after_middle = models.ImageField(
        upload_to='projects/content/',
        verbose_name="Imagen después de Middle",
        help_text="Se muestra entre middle y conclusion (ej: resultados, screenshots)",
        blank=True,
        null=True
    )
    
    video_url = models.URLField(
        blank=True, 
        default='', 
        verbose_name="Video URL",
        help_text="YouTube, Vimeo, etc."
    )
    
    # ===========================================
    # ENLACES EXTERNOS
    # ===========================================
    github_url = models.URLField(
        blank=False, 
        default='', 
        verbose_name="GitHub URL"
    )
    demo_url = models.URLField(
        blank=True,
        default='', 
        verbose_name="Demo URL"
    )
    
    # ===========================================
    # TECNOLOGÍAS Y METADATA
    # ===========================================
    technologies = models.ManyToManyField(
        'Technology',
        related_name='projects',
        verbose_name="Technologies",
        blank=True
    )
    skills = models.ManyToManyField(
        'Skill',
        related_name='projects',
        verbose_name="Skills",
        blank=True
    )
    
    # ===========================================
    # CONFIGURACIÓN Y ORDEN
    # ===========================================
    featured = models.BooleanField(
        default=False, 
        verbose_name="Featured",
        help_text="Show in featured projects section"
    )
    
    order = models.IntegerField(
        default=0, 
        verbose_name="Order",
        help_text="Lower numbers appear first"
    )
    
    # ===========================================
    # TIMESTAMPS
    # ===========================================
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Created at"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Updated at"
    )
    
    # ===========================================
    # CLASES INTERNAS Y MÉTODOS
    # ===========================================
    class Meta:
        ordering = ['order', '-created_at']
        verbose_name = "Project"
        verbose_name_plural = "Projects"
    
    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    # ===========================================
    # PROPIEDADES PARA TRADUCCIÓN
    # ===========================================
    @property
    def get_title(self):
        """Devuelve el título según el idioma activo."""
        lang = get_language()
        return getattr(self, f'title_{lang}', self.title)
    
    @property
    def get_short_description(self):
        """Devuelve la descripción corta según el idioma activo."""
        lang = get_language()
        return getattr(self, f'short_description_{lang}', self.short_description)
    
    @property
    def get_body_html_intro(self):
        """Devuelve la introducción según el idioma activo."""
        lang = get_language()
        return getattr(self, f'body_html_intro_{lang}', self.body_html_intro)
    
    @property
    def get_body_html_middle(self):
        """Devuelve el contenido medio según el idioma activo."""
        lang = get_language()
        return getattr(self, f'body_html_middle_{lang}', self.body_html_middle)
    
    @property
    def get_body_html_conclusion(self):
        """Devuelve la conclusión según el idioma activo."""
        lang = get_language()
        return getattr(self, f'body_html_conclusion_{lang}', self.body_html_conclusion)