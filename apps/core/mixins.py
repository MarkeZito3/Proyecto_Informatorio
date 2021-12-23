from django.core.exceptions     import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
#voy a modificar el mixind de LoginRequiredMixin

class LoginRequiredMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        return redirect('index')

class AdminRequiredMixins():
	# permisos_requeridos = []
	def dispatch(self, request, *args, **kwars):
		# print(self.permisos_requeridos)
		if not request.user.es_administrador:
			return redirect('index')
		return super(AdminRequiredMixins, self).dispatch(request, *args, **kwars)

class WriterRequiredMixins():
    def dispatch(self, request, *args, **kwars):
        if not request.user.es_writer and not request.user.es_administrador:
            return redirect('index')
        return super(WriterRequiredMixins, self).dispatch(request, *args, **kwars)

