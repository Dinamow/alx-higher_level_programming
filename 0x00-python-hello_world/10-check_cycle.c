#include "lists.h"
#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int check_cycle(listint_t *list)
{
	listint_t *temp;
	temp = list;
	while(list)
	{
		if (list->next == NULL)
			return (0);
		list = list->next;
		if (list == temp)
			return (1);
	}
}
