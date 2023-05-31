from django.shortcuts import render
from .upload_excel import BookResources, StudentResources
from accounts.models import Book, CustomUser, Group
from django.contrib import messages
from tablib import Dataset


def student_upload(request):
    if request.method == 'POST':
        dataset = Dataset()
        new_book = request.FILES['file']
        imported_data = dataset.load(new_book.read(), format='xlsx')
        i, x, q, s,n = 0, 0, "", 0,0
        for data in imported_data:
            print(i)
            i += 1
            group = data[12]
            print(Group.objects.filter(number=group))
            if Group.objects.filter(number=group):
                pass
            else:
                Group(number=group).save()
            group_id = Group.objects.get(number=group)
            try:
                user = CustomUser.objects.create_user(
                    username=data[0],
                    password=data[8],
                    user_type=3
                )
                user.student.FIO = data[1]
                user.student.passport_id = data[8]
                user.student.JSHSHIR = data[9]
                user.student.fuqarolik = data[2]
                user.student.country = data[3]
                user.student.region = data[5]
                user.student.tuman = data[6]
                user.student.gender = data[7]
                user.student.brithday = "Kiritilmagan"
                user.student.faculty = data[11]
                user.student.groups = group_id
                user.student.typeofEducation = data[16]
                user.student.formofEducation = data[17]
                user.student.phone_number = "Kiritilmagan"
                user.save()
                s+=1
            except Exception as e:
                print(f"upload_student error: {e}")
                x+=1
                q+=f"{i},"
        xato_s = ""
        if x:
            xato_s+=f"{x} nafar a'zo qo'shilmadi! "+q[:-1]+" - qatorlar"
        messages.success(request, f"{s} nafar a'zo qo'shildi!"+xato_s)
"""
        group = request.POST['group']
        dataset = Dataset()
        new_book = request.FILES['file']
        group_id = Group.objects.get(id=group)

        if not new_book.name.endswith('xlsx'):
            return render(request, 'staff/file_upload/upload.html')
        imported_data = dataset.load(new_book.read(), format='xlsx')
        i, x, q, s = 0, 0, "", 0
        for data in imported_data:
            i += 1
            try:
                user = CustomUser.objects.create_user(
                    username=data[15],
                    password=data[16],
                    user_type=3
                )
                user.student.FIO = data[1]
                user.student.passport_id = data[2]
                user.student.JSHSHIR = data[3]
                user.student.fuqarolik = data[4]
                user.student.country = data[5]
                user.student.region = data[7]
                user.student.tuman = data[8]
                user.student.gender = data[7]
                user.student.brithday = data[10]
                user.student.faculty = data[11]
                user.student.groups = group_id
                user.student.typeofEducation = data[12]
                user.student.formofEducation = data[13]
                user.student.phone_number = data[14]
                user.save()
                s+=1
            except Exception as e:
                print(f"upload_student error: {e}")
                x+=1
                q+=f"{i},"
        xato_s = ""
        if x:
            xato_s+=f"{x} nafar a'zo qo'shilmadi! "+q[:-1]+" - qatorlar"
        messages.success(request, f"{s} nafar a'zo qo'shildi!"+xato_s)

    context = {
        'group': [[]],
    }
    return render(request, 'staff/settings/upload_student_data.html', context)
    return render(request, 'staff/settings/upload_book_data.html')
"""
    return render(request, 'staff/settings/upload_book_data.html')


def book_upload1(request):
    """
    book upload view
    """
    if request.method == 'POST':
        try:
            dataset = Dataset()
            new_book = request.FILES['file']

            if not new_book.name.endswith('xlsx'):
                return render(request, 'staff/file_upload/book_upload.html')
            imported_data = dataset.load(new_book.read(), format='xlsx')
            book_c = 0
            for data in imported_data:
                if data[1] and data[2] and data[3] and data[4] and data[5] and data[6] and data[7] and data[8] and data[9] and data[10] and data[11]:
                    book_c += 1
                    value = Book(
                        book_name=data[1],
                        author=data[2],
                        organization=data[3],
                        publishing=data[4],
                        book_type=data[5],
                        language=data[6],
                        year=data[7],
                        beti=data[8],
                        isbn=data[9],
                        money=data[10],
                        key=data[11],
                    )
                    value.save()
                else:
                    break
            messages.success(request, f"{book_c} ta kitob qo'shildi!")
        except Exception as e:
            messages.success(request, "Ma'lumotlarni yuklash mobaynida xatolik yuzaga keldi!")
    return render(request, 'staff/settings/upload_book_data.html')



def book_upload(request):
    """
    book upload view
    """
    Book.objects.all().delete()
    if request.method == 'POST':
        dataset = Dataset()
        new_book = request.FILES['file']

        if not new_book.name.endswith('xlsx'):
            return render(request, 'staff/file_upload/book_upload.html')
        imported_data = dataset.load(new_book.read(), format='xlsx')
        book_c = 0
        ids = []
        n = -1
        err = []
        use_data = []
        for data in imported_data:
            # if data[1] or data[2] or data[3] or data[4] or data[5] or data[6] or data[7] or data[8] or data[9] or data[10] or data[11]:
            n += 1
            if data[2]:use_data = data
            if data[3]:
                if data[3] in ids:
                    err.append("Qator: " + str(n) + " Sabab: Takrorlangan! Qiymat: " + str(data[3]))
                elif str(data[3]).isdigit():
                    ids.append(data[3])
                    book_c += 1
                    try:
                        value = Book(
                        book_name=use_data[2],
                        author=use_data[5],
                        organization=use_data[7],
                        publishing=use_data[6],
                        book_type=use_data[9],
                        language=use_data[10],
                        year=use_data[11],
                        beti=use_data[13],
                        isbn=use_data[14],
                        money=use_data[15],
                        key=data[3],
                        )
                        value.save()
                    except Exception as e:
                        err.append("Qator: " + str(n) + " Sabab: "+str(e)+" Qiymat: " + str(data[3]))
                else:
                    err.append("Qator: " + str(n) + " Sabab: " + str("Ma'lumot turi noto'g'ri") + " Qiymat: " + str(data[3]))
            elif not str(data[3]).isdigit():
                    err.append("Qator: " + str(n) + " Sabab: Qiymat mavjud emas! Qiymat: " + str(data[3]))
            else:
                err.append("Qator: " + str(n)+" Sabab: Malumot mavjud emas! Qiymat: " + str(data[3]))
        messages.success(request, f"{book_c} ta kitob qo'shildi!")
        # except Exception as e:
        #     print(e)
        #     print(use_data)
        #     messages.success(request, "Ma'lumotlarni yuklash mobaynida xatolik yuzaga keldi!")
        print(err)
    return render(request, 'staff/settings/upload_book_data.html')
