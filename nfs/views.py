from django.utils import timezone
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, permission_classes
import datetime
from rest_framework.response import Response
from accounts.models import NfcCheck, Students, Accept_Book, Staffs, Book
from datetime import timedelta


@api_view(['POST'])
@permission_classes([])
def nfs_accept_code(request):
    nfc_connect = request.data
    data = nfc_connect.get('name')

    student = get_object_or_404(Students, nfcId=data)

    book_key = NfcCheck.objects.get(student=student).key
    respite = NfcCheck.objects.get(student=student).respite

    Accept_Book.objects.create(
        student=student,
        staff=request.user,
        book_name=Book.objects.get(key=book_key).book_name,
        author=Book.objects.get(key=book_key).author,
        key=book_key,
        respite=respite,
    )
    nfs_obj = get_object_or_404(NfcCheck, id=NfcCheck.objects.get(key=book_key).id)
    nfs_obj.delete()
    obj = get_object_or_404(Book, id=Book.objects.get(key=book_key).id)
    obj.delete()

    return Response({'success': 'Book accepted successfully.'})
