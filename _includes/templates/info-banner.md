<div class="info-banner" style="display:none">
    <img src="/images/doc-info-icon.svg"/>
    <div>
      {% if include.title %}
      <div class="info-title">{{ include.title }}</div>
      {% endif %}
      {{ include.content | markdownify }}
    </div>
</div>
