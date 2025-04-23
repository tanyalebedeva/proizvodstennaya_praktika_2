{{- define "myapp-chart.name" -}}
{{- .Chart.Name | lower -}}
{{- end -}}

{{- define "myapp-chart.fullname" -}}
{{- include "myapp-chart.name" . }}-{{ .Release.Name }}
{{- end -}}
