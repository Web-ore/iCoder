from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.urls import reverse
import random
# Create your views here.
from .models import Ads
# Home Ads
class HA_Dashboard(ListView):
   model = Ads
   context_object_name = 'Haa'
   template_name = "Ads/List.html"
   ordering = "Position_Number"

   def post(self, request):
      GroupName = request.POST.get('gn')
      sa = Ads.objects.filter(Shifted=GroupName)
      arl = []
      term = 0
      # Deleting ADs
      pk = request.POST.get('adcosub')
      if pk != None:
         da = Ads.objects.filter(pk=pk)
         da.delete()
         # rearranging the Pos-numbers of Ads
         shifting(arl, sa, "")

      #suffle
      s1 = request.POST.get('shuffle')
      if s1 == "shuffle":
         random.shuffle(arl)
         #shuffle the pos-Number of Ads
         shifting(arl, sa, "shuffle")
         print(sa, arl)

      # Shifting Position
      sp = request.POST.get("spv") #where to shift value
      if sp:
         mad = request.POST.get("mad") #the one to shift value
         print(sp)
         ssad = sa.get(Position_Number=sp)# shifting with
         mmad = sa.get(Position_Number=mad)# shifting one
         mmad.Position_Number = sp
         mmad.save()
         ssad.Position_Number = mad
         ssad.save()

         print(sp, ssad)
      #    ad.Position_Number = sp
      #    ad.save()

      #    sad = Ads.objects.filter(Position_Number=sp).first()
      #    sad.Position_Number = mad
      #    sad.save()
      
      return redirect("AdsList")
   
   def get_context_data(self, *args, **kwargs): #same as context
      context = super(HA_Dashboard, self).get_context_data(**kwargs)

      context.update({
            'mirror': Ads.objects.filter(Shifted="Home").count(),
            'grp':"Home",
            "Ads": Ads.objects.filter(Shifted="Home"),
            "tat":Ads.objects.filter(Shifted="Home"),
            'disable':'',
        })
      return context

# Top-Tips Ads
class TTA_Dashboard(ListView):
   model = Ads
   context_object_name = 'Haa'
   template_name = "Ads/List.html"
   ordering = "Position_Number"

   def post(self, request):
      GroupName = request.POST.get('gn')
      sa = Ads.objects.filter(Shifted=GroupName)
      arl = []
      term = 0
      # Deleting ADs
      pk = request.POST.get('adcosub')
      if pk != None:
         da = Ads.objects.filter(pk=pk)
         da.delete()
         # rearranging the Pos-numbers of Ads
         shifting(arl, sa, "")

      #suffle
      s1 = request.POST.get('shuffle')
      if s1 == "shuffle":
         random.shuffle(arl)
         #shuffle the pos-Number of Ads
         shifting(arl, sa, "shuffle")
         print(sa, arl)
      return redirect("TopTipAdsList")
   
   def get_context_data(self, *args, **kwargs): #same as context
      context = super(TTA_Dashboard, self).get_context_data(**kwargs)

      context.update({
            'mirror': Ads.objects.filter(Shifted="Top-Tips").count(),
            'grp':"Top-Tips",
            "Ads": Ads.objects.filter(Shifted="Top-Tips"),
            'disable':'',
        })
      return context

# Search Ads
class SA_Dashboard(ListView):
   model = Ads
   context_object_name = 'Haa'
   template_name = "Ads/List.html"
   ordering = "Position_Number"

   def post(self, request):
      GroupName = request.POST.get('gn')
      sa = Ads.objects.filter(Shifted=GroupName)
      arl = []
      term = 0
      # Deleting ADs
      pk = request.POST.get('adcosub')
      if pk != None:
         da = Ads.objects.filter(pk=pk)
         da.delete()
         # rearranging the Pos-numbers of Ads
         shifting(arl, sa, "")

      #suffle
      s1 = request.POST.get('shuffle')
      if s1 == "shuffle":
         random.shuffle(arl)
         #shuffle the pos-Number of Ads
         shifting(arl, sa, "shuffle")
         print(sa, arl)
      return redirect("SearchAdsList")
   
   def get_context_data(self, *args, **kwargs): #same as context
      context = super(SA_Dashboard, self).get_context_data(**kwargs)

      context.update({
            'mirror': Ads.objects.filter(Shifted="Search").count(),
            'grp':"Search",
            "Ads": Ads.objects.filter(Shifted="Search"),
            'disable':'',
        })
      return context




class Ads_Create(CreateView):
   template_name = "Ads/Create.html"
   model = Ads
   context_object_name = "model"
   fields = [
         "Position_Number",
        "Ads_Name",
        "Ads_HTML",
        "Visibility",
        "Type",
        "Shifted",
        "tags",
   ]

   def get_success_url(self):
      return reverse('AdsList')
   
   def get_initial(self):
      initial_data = super().get_initial()
      # Group name
      grp = self.kwargs["grp"]
      # Pos-number
      adc = Ads.objects.filter(Shifted=grp).count()
      initial_data["Position_Number"] = adc+1
      # Shifted
      initial_data["Shifted"] = grp
      return initial_data

   def get_context_data(self, *args, **kwargs): #same as context
      context = super(Ads_Create, self).get_context_data(**kwargs)

      context.update({
            'grp':self.kwargs["grp"],
            'disable':'disabled',
        })
      return context

class Ads_Edit(UpdateView):
   template_name = "Ads/Edit.html"
   model = Ads
   context_object_name = "model"
   fields = [
        'Status',
        'Position_Number',
        "Ads_Name",
        "Ads_HTML",
        "Visibility",
        "Type",
        "Shifted",
        'tags',
   ]

   def get_initial(self):
      initial_data = super().get_initial()
      initial_data["Status"] = "Edit"
      return initial_data

   def get_success_url(self):
      return reverse('AdsList')
   
   def get_context_data(self, *args, **kwargs): #same as context
      context = super(Ads_Edit, self).get_context_data(**kwargs)

      context.update({
            'grp':Ads.objects.get(pk=self.get_object().pk).Shifted,
            'disable':'disabled',
        })
      return context
   
class Group(ListView):
   model = Ads
   context_object_name = "models"
   template_name = "Ads/Group.html"

   def get_context_data(self, *args, **kwargs): #same as context
      context = super(Group, self).get_context_data(**kwargs)
      x = self.request.GET.get("grp")
      print(x)
      if x != None:
         histor = Ads.objects.filter(Shifted=x)
         exter = "block"
      else:
         histor = Ads.objects.none()
         exter = "none"

      grp = []
      for i in Ads.objects.all():
         if not i.Shifted in grp:
            grp.append(i.Shifted)
         else:
            pass

      context.update({
         "grp":grp,
         'active':exter,
         'lg':histor,
         'gn':x,
         'mirror': histor.count(),
        })
      return context

   def post(self, request):
      ad = request.POST.get("adcosub")
      grp = request.POST.get("gn")
      spv = request.POST.get("spv")
      print(ad, grp, spv)
      return redirect("Group")


def shifting(varList, varQueryset, UniqueValue):
      term = 0
      for i in range(1, varQueryset.count()+1):
         varList.append(i) # collecting number of series
      
      # unique value integration
      if UniqueValue == "shuffle":
         random.shuffle(varList)
      else:
         pass
      # now adding the series of numbers to the ads
      for ad in varQueryset:
         if varQueryset.count()>1:
            ad.Position_Number = varList[term]
            ad.save()
            term = term+1
            
         if varQueryset.count()==1:
            ad.Position_Number = 1
            ad.save()

