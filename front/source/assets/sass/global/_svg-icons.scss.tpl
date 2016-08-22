<%= '// This file was generated with Gulp, do not edit' %>

$svg-icons: (<% icons.forEach(function (icon) { %>
  '<%= icon.name %>': '<%= icon.content %>',<% }) %>);

@mixin svg-icon ($name) {
  background-image: url("data:image/svg+xml;charset=utf8,#{ map-get($svg-icons, $name) }");
}
