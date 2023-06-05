#include "lists.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int check_cycle(listint_t *list)
{
	listint_t *temp;
	temp = list;
	list = list->next;
	while(list)
	{
		list = list->next;
		if (list == temp)
			return (1);
		temp = temp->next;
	}
	return (0);
}
